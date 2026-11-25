import os
root = "01_제철시금치_숏츠"
lines = [
 ("0~3","시금치, 아직도 아무 때나 드세요?",
  "Extreme close-up of fresh vibrant green winter spinach leaves covered in morning frost and tiny water droplets, dramatic bright natural light, shallow depth of field, high-resolution food photography, fresh and crisp mood, no text, no letters --ar 9:16 --v 6"),
 ("3~8","겨울 시금치는 추위를 견디며 단맛과 영양이 꽉 차요.",
  "Korean winter spinach growing low in a snowy farm field at sunrise, flat rosette-shaped leaves with red roots, soft golden natural light, sparkling frost, high-resolution photography, fresh and clean, no text, no letters --ar 9:16 --v 6"),
 ("8~13","첫째, 베타카로틴! 눈 건강과 면역력을 지켜줘요.",
  "Clean 3D infographic style illustration, glowing orange beta-carotene molecules floating out of a fresh green spinach leaf toward a stylized human eye and a protective shield icon, white bright background, soft studio lighting, minimal, no text, no letters --ar 9:16 --v 6"),
 ("13~18","둘째, 엽산! 새 세포와 혈액 생성에 꼭 필요해요.",
  "Clean 3D infographic style render, fresh spinach leaf surrounded by glowing healthy cells dividing and bright red blood cells flowing, soft pastel green and white background, bright natural light, minimal and clean, no text, no letters --ar 9:16 --v 6"),
 ("18~24","셋째, 철분과 루테인! 빈혈 예방과 눈 노화 방지까지.",
  "Split composition 3D infographic, top: spinach leaf with shiny metallic iron particles and energetic red blood cells, bottom: golden-yellow lutein glow protecting a healthy eye, bright clean white background, soft natural light, no text, no letters --ar 9:16 --v 6"),
 ("24~30","꿀팁! 30초만 살짝 데쳐 수산을 빼고,",
  "Fresh spinach being briefly blanched in a pot of boiling water, rising steam, a hand lifting bright green spinach with tongs into a bowl of ice water, bright kitchen with natural window light, high-resolution food photography, no text, no letters --ar 9:16 --v 6"),
 ("30~35","참기름이나 참깨와 함께 먹으면 흡수율이 쑥 올라가요.",
  "Korean seasoned spinach side dish (sigeumchi namul) in a white ceramic bowl, drizzled with glossy sesame oil and sprinkled with roasted sesame seeds, wooden table, bright natural daylight, top-down angle, high-resolution food photography, appetizing, no text, no letters --ar 9:16 --v 6"),
 ("35~38","더 많은 건강 꿀팁, 구독과 좋아요!",
  "Bright cheerful flat-lay of a fresh spinach bunch, sesame seeds and a bowl of spinach namul on a clean white marble table, generous empty space in the upper and lower area for overlay, soft natural light, fresh green and white palette, no text, no letters --ar 9:16 --v 6"),
]
os.makedirs(root, exist_ok=True)
for d in ["00_대본","09_BGM_효과음","10_최종출력"]:
    os.makedirs(f"{root}/{d}", exist_ok=True)
full = "\n".join(l[1] for l in lines)+"\n"
open(f"{root}/00_대본/full_script_vrew.txt","w").write(full)
for i,(t,s,p) in enumerate(lines,1):
    d=f"{root}/Scene_{i:02d}"; os.makedirs(d,exist_ok=True)
    open(f"{d}/S{i:02d}_script.txt","w").write(s+"\n")
    open(f"{d}/S{i:02d}_prompt.txt","w").write(p+"\n")
    open(f"{d}/S{i:02d}_README.txt","w").write(f"예상 시간: {t}초\n이 폴더에 생성한 이미지를 S{i:02d}_img.png 로 저장하세요.\n")
open(f"{root}/09_BGM_효과음/README.txt","w").write("BGM: bgm_main.mp3 / 효과음: sfx_01_whoosh.mp3, sfx_02_ding.mp3 형식으로 저장\n")
open(f"{root}/10_최종출력/README.txt","w").write("최종 영상: 제철시금치_숏츠_v1.mp4 / 썸네일: thumbnail.png\n")
print(len(full.replace("\n"," ").strip()), "chars incl spaces")
