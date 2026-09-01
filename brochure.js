const brochureChapters=[
["John to the Jordan: Source-Layer Orientation","约翰走向约旦河：来源层导览"],["Wilderness Life","旷野生活"],["Jordan and the Crowds","约旦河与人群"],["John's Social Ethics","约翰的社会伦理"],["Repentance, Fruit, and Judgment","悔改、果实与审判"],["The Stronger One Comes","那更有能力者将来"],
["Jesus Walks Toward the Jordan","耶稣走向约旦河"],["Mark: Earliest Extant Baptism Narrative","马可：最早现存的受洗叙事"],["Matthew: John's Objection Added","马太：加入约翰的反对"],["Luke: The Baptizer Recedes","路加：施洗者退到幕后"],["John: Baptism Reframed as Witness","约翰：受洗被重构为见证"],["John's Disciples","约翰的门徒"],["Jesus' Disciples","耶稣的门徒"],["Baptism and Purification Dispute","施洗与洁净之争"],["He Must Increase","他必兴旺"],
["John Challenges Herod","约翰挑战希律"],["Imprisonment","监禁"],["Are You the Coming One?","那将要来的是你吗？"],["Jesus Answers with Deeds","耶稣以行动回应"],["Jesus Evaluates John","耶稣评价约翰"],["Gospel Death Tradition","福音书中的死亡传统"],["Josephus: Political Threat Account","约瑟夫斯：政治威胁叙事"],["John's Disciples Bury Him","约翰的门徒埋葬他"],["Jesus Hears the News","耶稣听见消息"],
["After John Was Handed Over","约翰被交出去之后"],["The Kingdom Has Drawn Near","天国临近"],["Healing","医治"],["Table Fellowship with the Excluded","与被排斥者同席"],["Forgiveness","赦免"],["Sabbath","安息日"],["Seed and Sowing","种子与撒种"],["Storm and Fear","风暴与恐惧"],["Bread and Sharing","饼与分享"],["Power and Service","权力与服事"],["Entering Jerusalem","进入耶路撒冷"],["Death and Empty Tomb","死亡与空墓"],
["Witness to the Light","为光作见证"],["Living Water","活水"],["Bread of Life","生命之粮"],["Light of the World","世界的光"],["Good Shepherd","好牧人"],["The Vine","葡萄树"],["Love One Another","彼此相爱"],["Peace Be with You","愿你们平安"]
];
const brochurePhases=[
{range:[1,6],en:"THE WITNESS",zh:"见证者",color:"#b68a32"},
{range:[7,15],en:"THE WATER",zh:"水",color:"#405b63"},
{range:[16,24],en:"THE COST OF WITNESS",zh:"见证的代价",color:"#b94d48"},
{range:[25,36],en:"THE WAY OPENS",zh:"道路展开",color:"#2f6a4f"},
{range:[37,44],en:"LIGHT & LOVE",zh:"光与爱",color:"#b68a32"}
];
const chapterRoot=document.querySelector("#brochure-chapters");
brochurePhases.forEach((phase,index)=>{
  const section=document.createElement("section");
  section.className="phase-block";
  const cards=brochureChapters.slice(phase.range[0]-1,phase.range[1]).map((chapter,offset)=>{
    const number=phase.range[0]+offset;
    return `<article class="chapter-mini" style="--phase-color:${phase.color}"><b>${String(number).padStart(2,"0")}</b><strong>${chapter[1]}</strong><small>${chapter[0]}</small></article>`;
  }).join("");
  section.innerHTML=`<div class="phase-title"><strong>0${index+1}</strong><h3>${phase.zh} · ${phase.en}</h3><span>CH. ${String(phase.range[0]).padStart(2,"0")}–${String(phase.range[1]).padStart(2,"0")}</span></div><div class="chapter-mini-grid">${cards}</div>`;
  chapterRoot.append(section);
});
