# https://github.com/Dragonfly-Chat/emoji
VERSION = "0.0.2"
import os, json

config = {
  "path": "/emoji/",
  "size": "32px",
  "js_title_includes_version": True
}

if os.path.exists("emoji-build.json") and os.path.isfile("emoji-build.json"):
  config_in_file = open("emoji-build.json")
  config_in = json.loads(config_in_file.read())
  config_in_file.close()
  for c in config_in.keys():
    config[c] = config_in[c]

if os.path.exists("build"):
  print("Build directory exists, clearing build...")
  for file in os.listdir("build/emoji"):
    os.remove(f"build/emoji/{file}")
  for file in os.listdir("build"):
    if os.path.isfile(file):
      os.remove(f"build/{file}")
else:
  print("Creating build directories...")
  os.mkdir("build")
  os.mkdir("build/emoji")
print("Done.")

print("Building emojis...")
emojilist = []
for category in os.listdir("assets/community"):
  for file in os.listdir(f"assets/community/{category}"):
    infile = open(f"assets/community/{category}/{file}", 'rb')
    emoji_name = f"{category}_{file.split('.')[0]}"
    emojilist.append(emoji_name)
    outfile = open(f"build/emoji/{emoji_name}", 'wb')
    outfile.write(infile.read())
    infile.close()
    outfile.close()
print("Done.")



print("Building JavaScript library...")
js = """
/* Dragonfly emoji set v%ver%. Licensed under MIT. All credit goes to contributors. */ 
$_emoji={
  p:'%path%',
  s:'%size%',
  v:'%ver%',
  u:function(e=""){
    return this.p+e;
  },
  const:function(e="",size=""){
    return '<img src="'+this.u(e)+'" width="'+size+'" height="'+size+'" alt="'+e+'" class="emoji"/>';
  },
  c:function(e=""){
    em=e.split(':')[1];
    if(this.list.includes(em)){
      return this.const(em,this.s);
    }else{
      return e;
    }
  },
  text:function(t=""){
    var el=t.match(/:(\S.\S*?):/g);
    var rl=[];
    el.forEach((e)=>{
      t=t.replace(e,this.c(e));
    });
    return t;
  },
  list:JSON.parse('%list%'),
  element:function(el){
    el.innerHTML=this.text(el.innerHTML);
  },
  element_query:function(qs=""){
    this.element(document.querySelector(qs));
  },
  element_query_all:function(qs=""){
    var queries=document.querySelectorAll(qs);
    for(var i=0;i<queries.length;i++){
      this.element(queries[i]);
    }
  },
  element_id:function(id=""){
    this.element_query('#'+id);
  }
}
"""

# Minify, build, & save JavaScript file
if config['js_title_includes_version']:
  js_filename = f"build/dragonfly-emoji-{VERSION}.min.js"
else:
  js_filename = "build/dragonfly-emoji.min.js"
js_file = open(js_filename, 'w')
js_file.write(js.replace('\n','').replace('  ','').replace('%path%', config['path']).replace('%size%', config['size']).replace('%ver%', VERSION).replace('%list%', json.dumps(emojilist)))
js_file.close()
print("Done.")
