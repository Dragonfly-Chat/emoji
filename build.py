# https://github.com/Dragonfly-Chat/emoji
VERSION = "0.0.1"
import os, json

config = {
  "path": "/emoji/",
  "size": "32px"
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
  c:function(e=""){
    em=e.split(':')[1];
    if(this.list.includes(em)){
      return '<img src="'+this.u(em)+'" width="'+this.s+'" height="'+this.s+'" alt="'+em+'" class="emoji"/>';
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
  list:JSON.parse('%list%')
}
"""

# Minify, build, & save JavaScript file
js_file = open(f"build/dragonfly-emoji-{VERSION}.min.js", 'w')
js_file.write(js.replace('\n','').replace('  ','').replace('%path%', config['path']).replace('%size%', config['size']).replace('%ver%', VERSION).replace('%list%', json.dumps(emojilist)))
js_file.close()
print("Done.")
