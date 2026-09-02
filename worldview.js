import * as maplibregl from "https://unpkg.com/maplibre-gl@6.6.0/dist/maplibre-gl.mjs";

const chapterTitles = [
  ["John to the Jordan: Source-Layer Orientation","约翰走向约旦河：来源层导览"],["Wilderness Life","旷野生活"],["Jordan and the Crowds","约旦河与人群"],["John's Social Ethics","约翰的社会伦理"],["Repentance, Fruit, and Judgment","悔改、果实与审判"],["The Stronger One Comes","那更有能力者将来"],
  ["Jesus Walks Toward the Jordan","耶稣走向约旦河"],["Mark: Earliest Extant Baptism Narrative","马可：最早现存的受洗叙事"],["Matthew: John's Objection Added","马太：加入约翰的反对"],["Luke: The Baptizer Recedes","路加：施洗者退到幕后"],["John: Baptism Reframed as Witness","约翰：受洗被重构为见证"],
  ["John's Disciples","约翰的门徒"],["Jesus' Disciples","耶稣的门徒"],["Baptism and Purification Dispute","施洗与洁净之争"],["He Must Increase","他必兴旺"],["John Challenges Herod","约翰挑战希律"],["Imprisonment","监禁"],["Are You the Coming One?","那将要来的是你吗？"],["Jesus Answers with Deeds","耶稣以行动回应"],["Jesus Evaluates John","耶稣评价约翰"],["Gospel Death Tradition","福音书中的死亡传统"],["Josephus: Political Threat Account","约瑟夫斯：政治威胁叙事"],["John's Disciples Bury Him","约翰的门徒埋葬他"],["Jesus Hears the News","耶稣听见消息"],
  ["After John Was Handed Over","约翰被交出去之后"],["The Kingdom Has Drawn Near","天国临近"],["Healing","医治"],["Table Fellowship with the Excluded","与被排斥者同席"],["Forgiveness","赦免"],["Sabbath","安息日"],["Seed and Sowing","种子与撒种"],["Storm and Fear","风暴与恐惧"],["Bread and Sharing","饼与分享"],["Power and Service","权力与服事"],["Entering Jerusalem","进入耶路撒冷"],["Death and Empty Tomb","死亡与空墓"],
  ["Witness to the Light","为光作见证"],["Living Water","活水"],["Bread of Life","生命之粮"],["Light of the World","世界的光"],["Good Shepherd","好牧人"],["The Vine","葡萄树"],["Love One Another","彼此相爱"],["Peace Be with You","愿你们平安"]
];

const previewImages = {
  1: "/from-john-to-jesus/season-01/batch-01-john-to-jordan/final/01-john-appears.png",
  2: "/from-john-to-jesus/season-01/batch-01-john-to-jordan/final/02-jordan-crowds.png",
  3: "/assets/chapters/chapter-03-jordan-and-the-crowds-v1.png",
  4: "/assets/chapters/chapter-04-johns-social-ethics-v1.png",
  6: "/from-john-to-jesus/season-01/batch-01-john-to-jordan/final/06-mark-baptism.png",
  8: "/from-john-to-jesus/season-01/batch-01-john-to-jordan/final/08-let-it-be-so-now.png",
  10: "/from-john-to-jesus/season-01/batch-01-john-to-jordan/final/10-john-witnesses.png"
};

const events = [
  {id:"voice",range:[1,6],eventTime:"c. 28 CE",layer:"event",timeZh:"神圣事件",timeEn:"Sacred event",zh:"旷野里的声音",en:"THE VOICE IN THE WILDERNESS",place:"犹太旷野 · Judean Wilderness",center:[35.35,31.72],zoom:8.1,cards:"♠ A–3 · ♦ A–3 · ♣ A–4",descZh:"约翰作为声音进入故事；旷野不是空白背景，而是旧先知传统重新被唤醒的地方。",descEn:"John enters as a voice. The wilderness is not empty scenery but a reawakening of prophetic memory."},
  {id:"jordan",range:[7,11],eventTime:"c. 28 CE",layer:"event",timeZh:"神圣事件",timeEn:"Sacred event",zh:"约旦河与施洗",en:"THE JORDAN & THE BAPTISM",place:"约旦河 · Jordan River",center:[35.55,31.84],zoom:9.2,cards:"♠ A · ♦ A · ♣ A · ♥ A",descZh:"同一条河流承载四种叙事安排：事件、对话、重排与见证。",descEn:"One river carries four narrative arrangements: event, dialogue, reframing, and witness."},
  {id:"disciples",range:[12,15],eventTime:"c. 28–29 CE",layer:"event",timeZh:"神圣事件",timeEn:"Sacred event",zh:"门徒与洁净之争",en:"DISCIPLES & PURIFICATION",place:"犹太地 · Judea",center:[35.37,31.98],zoom:8.3,cards:"♠ 4–5 · ♦ 4–5 · ♣ 5 · ♥ 2–4",descZh:"两组门徒、施洗与洁净之争，使使命交接第一次成为公开问题。",descEn:"Two circles of disciples and a dispute over purification make the handover a public question."},
  {id:"prison",range:[16,20],eventTime:"c. 29 CE",layer:"event",timeZh:"神圣事件",timeEn:"Sacred event",zh:"权力、监禁与疑问",en:"POWER, PRISON & DOUBT",place:"马盖鲁斯 · Machaerus",center:[35.62,31.57],zoom:9,cards:"♠ 6–8 · ♦ 6–8 · ♣ 6–8",descZh:"见证者挑战权力，又在监狱中发出未被简化的疑问。",descEn:"The witness confronts power, then voices an unresolved question from prison."},
  {id:"death",range:[21,24],eventTime:"c. 29 CE",layer:"event",timeZh:"神圣事件",timeEn:"Sacred event",zh:"见证者之死",en:"THE DEATH OF THE WITNESS",place:"死海东岸 · East of the Dead Sea",center:[35.58,31.61],zoom:8.7,cards:"♠ Q · ♦ Q · historical witness",descZh:"死亡不是支线结局，而是使命交接的叙事铰链。",descEn:"Death is not a side ending; it becomes the narrative hinge of the handover."},
  {id:"galilee",range:[25,34],eventTime:"c. 29–30 CE",layer:"event",timeZh:"神圣事件",timeEn:"Sacred event",zh:"道路在加利利展开",en:"THE WAY OPENS IN GALILEE",place:"加利利 · Galilee",center:[35.52,32.78],zoom:8.2,cards:"♠ 9–K · Synoptic parallels",descZh:"约翰被交出去以后，耶稣的使命沿马可最早现存的叙事骨架展开。",descEn:"After John is handed over, Jesus' mission unfolds along Mark's earliest extant narrative spine."},
  {id:"jerusalem",range:[35,36],eventTime:"c. 30 CE",layer:"event",timeZh:"神圣事件",timeEn:"Sacred event",zh:"耶路撒冷、死亡与空墓",en:"JERUSALEM, DEATH & EMPTY TOMB",place:"耶路撒冷 · Jerusalem",center:[35.23,31.78],zoom:9.2,cards:"♠ K · ♦ K · ♣ K · ♥ K",descZh:"四条福音路线汇聚到权力中心，随后以不同方式记忆死亡与空墓。",descEn:"Four Gospel routes converge at the center of power, then remember death and the empty tomb differently."},
  {id:"light",range:[37,44],eventTime:"90–100 CE",layer:"gospel",timeZh:"福音记忆",timeEn:"Gospel memory",zh:"见证、光与爱",en:"WITNESS, LIGHT & LOVE",place:"约翰传统 · Johannine tradition",center:[35.23,31.78],zoom:7.7,cards:"♥ A–K · two Jokers",descZh:"最后八章进入较晚的约翰神学：水、生命、光、牧人、葡萄树、爱与平安。",descEn:"The final eight chapters enter the later Johannine theology of water, life, light, shepherd, vine, love, and peace."},
  {id:"mark",range:[25,36],eventTime:"65–75 CE",layer:"gospel",timeZh:"福音形成",timeEn:"Gospel composition",zh:"马可：最早现存骨架",en:"MARK: EARLIEST EXTANT SPINE",place:"文本形成层 · Text layer",center:[35.52,32.78],zoom:7.2,cards:"♠ MARK · A–K",descZh:"这里标注的是文本形成时间，不是故事事件发生时间。",descEn:"This marks the period of textual composition, not the date of the narrated events."},
  {id:"synoptics",range:[7,36],eventTime:"80–95 CE",layer:"gospel",timeZh:"福音形成",timeEn:"Gospel composition",zh:"马太与路加：扩写、重排",en:"MATTHEW & LUKE: EXPANSION",place:"文本形成层 · Text layer",center:[35.4,32.2],zoom:6.9,cards:"♦ MATTHEW · ♣ LUKE",descZh:"马太与路加分别扩写、解释和重排较早传统。",descEn:"Matthew and Luke expand, explain, and reorder earlier traditions in distinct ways."},
  {id:"john",range:[37,44],eventTime:"90–100 CE",layer:"gospel",timeZh:"福音形成",timeEn:"Gospel composition",zh:"约翰：见证、光与爱",en:"JOHN: WITNESS, LIGHT & LOVE",place:"文本形成层 · Text layer",center:[35.23,31.78],zoom:6.9,cards:"♥ JOHN · A–K",descZh:"事件被重构成见证，光、生命与爱成为神学高潮。",descEn:"Events are reframed as witness; light, life, and love become the theological climax."},
  {id:"papyrus",range:[1,44],eventTime:"c. 125–400 CE",layer:"manuscript",timeZh:"抄本见证",timeEn:"Manuscript witness",zh:"纸草、圣名与大型抄本",en:"PAPYRI, SACRED NAMES & CODICES",place:"现存见证层 · Surviving witnesses",center:[31.2,30.2],zoom:5.8,cards:"Ι̅C̅ · FOUR GOSPELS",descZh:"读者进入文本史：现存残片、圣名缩写与大型抄本塑造了我们今天能够比较的证据。",descEn:"The journey enters text history: fragments, sacred-name contractions, and major codices shape the evidence available today."}
];

const chapterPlaceholder = "/assets/chapter-placeholder.svg";
const suitStories = [
  {symbol:"♠",name:"MARK · 马可",image:"/assets/cards/ace-spades-mark.png",period:"c. 65–75 CE · A–K COMPLETE",zh:"最早现存的叙事骨架",en:"Earliest extant narrative spine"},
  {symbol:"♦",name:"MATTHEW · 马太",image:"/assets/cards/ace-diamonds-matthew.png",period:"c. 80–95 CE · IN PRODUCTION",zh:"扩写、解释与回应",en:"Expansion, explanation, response"},
  {symbol:"♣",name:"LUKE · 路加",image:"/assets/cards/ace-clubs-luke.png",period:"c. 80–95 CE · IN PRODUCTION",zh:"社会伦理与叙事重排",en:"Social ethics and reordered scenes"},
  {symbol:"♥",name:"JOHN · 约翰",image:"/assets/cards/ace-hearts-john.png",period:"c. 90–100 CE · IN PRODUCTION",zh:"见证、光与神学重构",en:"Witness, light, theological reframing"}
];

const route = events.filter(event=>event.layer==="event").map(event=>event.center);
const eventForChapter = chapter => events.find(event=>event.layer==="event" && chapter>=event.range[0] && chapter<=event.range[1]) || events[7];
const state = {chapter:7,event:events[1],map:null,markers:[],view:"geo",language:document.documentElement.dataset.lang||"zh"};

function copyForLanguage(zh,en){return state.language==="zh"?zh:en}

function selectChapter(chapter,fly=true){
  const event=eventForChapter(chapter);
  state.chapter=chapter;state.event=event;
  const title=chapterTitles[chapter-1];
  document.querySelector("#worldview-chapter").textContent=`CHAPTER ${String(chapter).padStart(2,"0")} / 44`;
  document.querySelector("#worldview-title").textContent=state.language==="zh"?title[1]:title[0];
  document.querySelector("#worldview-title-en").textContent=title[0].toUpperCase();
  document.querySelector("#worldview-description").textContent=copyForLanguage(event.descZh,event.descEn);
  document.querySelector("#worldview-place").textContent=event.place;
  document.querySelector("#worldview-time").textContent=`${event.eventTime} · ${copyForLanguage(event.timeZh,event.timeEn)}`;
  document.querySelector("#worldview-card-map").textContent=event.cards;
  const image=document.querySelector("#worldview-image");
  image.src=previewImages[chapter]||chapterPlaceholder;
  image.alt=`${title[0]} visual preview`;
  document.querySelector("#worldview-image-label").textContent=previewImages[chapter]?`CHAPTER ART · ${String(chapter).padStart(2,"0")} / 44`:`CHAPTER ${String(chapter).padStart(2,"0")} · IN RESEARCH`;
  document.querySelectorAll(".chapter-library-card").forEach(button=>button.setAttribute("aria-pressed",String(Number(button.dataset.chapter)===chapter)));
  document.querySelectorAll(".sacred-event").forEach(button=>button.setAttribute("aria-pressed",String(button.dataset.event===event.id)));
  state.markers.forEach(item=>item.element.classList.toggle("is-active",item.event.id===event.id));
  if(fly&&state.map)state.map.flyTo({center:event.center,zoom:event.zoom,pitch:52,bearing:event.center[1]>32?-18:10,duration:1800,essential:true});
}

function selectEvent(event){
  selectChapter(event.range[0],false);state.event=event;
  const range=event.range[0]===event.range[1]?String(event.range[0]).padStart(2,"0"):`${String(event.range[0]).padStart(2,"0")}–${String(event.range[1]).padStart(2,"0")}`;
  document.querySelector("#worldview-chapter").textContent=event.layer==="event"?`CHAPTER ${range} / 44`:event.eventTime;
  document.querySelector("#worldview-title").textContent=copyForLanguage(event.zh,event.en);
  document.querySelector("#worldview-title-en").textContent=event.en;
  document.querySelector("#worldview-description").textContent=copyForLanguage(event.descZh,event.descEn);
  document.querySelector("#worldview-place").textContent=event.place;
  document.querySelector("#worldview-time").textContent=`${event.eventTime} · ${copyForLanguage(event.timeZh,event.timeEn)}`;
  document.querySelector("#worldview-card-map").textContent=event.cards;
  const image=document.querySelector("#worldview-image");image.src=previewImages[event.range[0]]||chapterPlaceholder;image.alt=`${event.en} sacred-history preview`;
  document.querySelector("#worldview-image-label").textContent=previewImages[event.range[0]]?`CHAPTER ART · ${String(event.range[0]).padStart(2,"0")} / 44`:`SACRED HISTORY · CH. ${range}`;
  document.querySelectorAll(".sacred-event").forEach(button=>button.setAttribute("aria-pressed",String(button.dataset.event===event.id)));
  state.markers.forEach(item=>item.element.classList.toggle("is-active",item.event.id===event.id));
  if(state.map)state.map.flyTo({center:event.center,zoom:event.zoom,pitch:52,bearing:event.center[1]>32?-18:10,duration:1800,essential:true});
}

function buildChapterLibrary(){
  const grid=document.querySelector("#worldview-chapters");
  grid.innerHTML=chapterTitles.map((title,index)=>{
    const chapter=index+1;
    const hasPreview=Boolean(previewImages[chapter]);
    const status=hasPreview?(state.language==="zh"?"视觉预览已公开":"VISUAL PREVIEW LIVE"):(state.language==="zh"?"研究制作中":"IN RESEARCH");
    return `<button type="button" class="chapter-library-card${hasPreview?" has-preview":""}" data-chapter="${chapter}" aria-pressed="${chapter===state.chapter}" aria-label="Chapter ${chapter}: ${title[0]}"><b>${String(chapter).padStart(2,"0")}</b><span><strong>${state.language==="zh"?title[1]:title[0]}</strong><small>${status}</small></span></button>`;
  }).join("");
  grid.querySelectorAll("button").forEach(button=>button.addEventListener("click",()=>selectChapter(Number(button.dataset.chapter))));
}

function buildDeckWorld(){
  const container=document.querySelector("#worldview-deck");
  container.innerHTML=suitStories.map(suit=>`<article class="deck-world-suit"><img src="${suit.image}" alt="${suit.name} Gospel playing card"><div><h4>${suit.name}</h4><p><span data-copy="zh">${suit.zh}</span><span data-copy="en">${suit.en}</span></p><small>${suit.period}</small></div><b>${suit.symbol}</b></article>`).join("");
}

function buildTimeline(){
  const labels={event:["神圣事件","SACRED EVENTS"],gospel:["福音记忆与形成","GOSPEL MEMORY & COMPOSITION"],manuscript:["现存抄本见证","SURVIVING MANUSCRIPT WITNESSES"]};
  const container=document.querySelector("#sacred-timeline");
  container.innerHTML=["event","gospel","manuscript"].map(layer=>`<section class="timeline-lane"><header><span>${labels[layer][0]}</span><small>${labels[layer][1]}</small></header><div>${events.filter(event=>event.layer===layer).map(event=>`<button type="button" class="sacred-event" data-event="${event.id}" aria-pressed="${event.id==="jordan"}"><time>${event.eventTime}</time><span><b>${event.zh}</b><em>${event.en}</em><small>CH. ${String(event.range[0]).padStart(2,"0")}–${String(event.range[1]).padStart(2,"0")}</small></span><i>＋</i></button>`).join("")}</div></section>`).join("");
  container.querySelectorAll(".sacred-event").forEach(button=>button.addEventListener("click",()=>selectEvent(events.find(event=>event.id===button.dataset.event))));
}

function buildMap(){
  const map=new maplibregl.Map({container:"sacred-map",style:"https://tiles.openfreemap.org/styles/positron",center:[35.4,31.9],zoom:6.7,pitch:48,bearing:8,attributionControl:true});
  state.map=map;
  map.addControl(new maplibregl.NavigationControl({showCompass:true}),"bottom-left");
  map.on("load",()=>{
    map.addSource("sacred-route",{type:"geojson",data:{type:"Feature",properties:{},geometry:{type:"LineString",coordinates:route}}});
    map.addLayer({id:"sacred-route-glow",type:"line",source:"sacred-route",paint:{"line-color":"#c9a556","line-width":10,"line-opacity":.16,"line-blur":8}});
    map.addLayer({id:"sacred-route-line",type:"line",source:"sacred-route",paint:{"line-color":"#a9802d","line-width":3,"line-opacity":.9,"line-dasharray":[1.2,1.5]}});
    events.filter(event=>event.layer==="event").forEach(event=>{
      const element=document.createElement("button");element.type="button";element.className="sacred-map-marker";element.dataset.event=event.id;element.setAttribute("aria-label",`${event.en}, chapters ${event.range[0]} to ${event.range[1]}`);element.innerHTML=`<span>${String(event.range[0]).padStart(2,"0")}</span><small>${event.en}</small>`;element.addEventListener("click",()=>selectEvent(event));
      new maplibregl.Marker({element,anchor:"center"}).setLngLat(event.center).addTo(map);state.markers.push({element,event});
    });
    selectChapter(state.chapter,false);
  });
}

function setView(view){
  state.view=view;
  document.querySelectorAll("[data-world-view]").forEach(button=>button.setAttribute("aria-selected",String(button.dataset.worldView===view)));
  document.querySelectorAll("[data-world-panel]").forEach(panel=>panel.hidden=panel.dataset.worldPanel!==view);
  if(view==="geo"&&state.map)setTimeout(()=>state.map.resize(),50);
  if(view==="chapters")selectChapter(state.chapter,false);
}

document.querySelectorAll("[data-world-view]").forEach(button=>button.addEventListener("click",()=>setView(button.dataset.worldView)));
window.addEventListener("bible:language",event=>{state.language=event.detail.language;buildChapterLibrary();selectChapter(state.chapter,false)});
buildChapterLibrary();buildDeckWorld();buildTimeline();buildMap();selectChapter(state.chapter,false);
