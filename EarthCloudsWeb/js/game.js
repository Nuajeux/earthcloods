const repque1 = document.querySelector("#qu1");
const sol1 = document.querySelector("#solu1");

const repque2 = document.querySelector("#qu2");
const sol2 = document.querySelector("#solu2");

const repque3 = document.querySelector("#qu3");
const sol3 = document.querySelector("#solu3");

const repque4 = document.querySelector("#qu4");
const sol4 = document.querySelector("#solu4");

const repque5 = document.querySelector("#qu5");
const sol5 = document.querySelector("#solu5");


const bouton = document.querySelector("button");
	
const res = document.querySelector("p.resu");
const come = document.querySelector("p.com");

const yes1 = document.querySelector('#yes1');
const yes2 = document.querySelector('#yes2');
const yes3 = document.querySelector('#yes3');
const yes4 = document.querySelector('#yes4');
const yes5 = document.querySelector('#yes5');
const no1 = document.querySelector('#nop1');
const no2 = document.querySelector('#nop2');
const no3 = document.querySelector('#nop3');
const no4 = document.querySelector('#nop4');
const no5 = document.querySelector('#nop5');

let resultat = 0;

bouton.addEventListener("click",()=>{
 if(repque1.value===sol1.value){
 	repque1.style.color = "#0E5D24";
 	repque1.style.border = "1px solid #3CE68D";
 	resultat += 1;
 	yes1.style.visibility = "visible";
 	yes1.style.margin = "0px 0px 0px 20px";
 }else{
 	repque1.style.color = "#95171B";
 	repque1.style.border = "1px solid #C8102E";
 	no1.style.visibility = "visible";
 }

 if(repque2.value===sol2.value){
 	repque2.style.color = "#0E5D24";
 	repque2.style.border = "1px solid #3CE68D";
 	resultat += 1;
 	yes2.style.visibility = "visible";
 	yes2.style.margin = "0px 0px 0px 20px";
 }else{
 	repque2.style.color = "#95171B";
 	repque2.style.border = "1px solid #C8102E";
 	no2.style.visibility = "visible";
 }
 if(repque3.value===sol3.value){
 	repque3.style.color = "#0E5D24";
 	repque3.style.border = "1px solid #3CE68D";
 	resultat += 1;
 	yes3.style.visibility = "visible";
 	yes3.style.margin = "0px 0px 0px 20px";
 }else{
 	repque3.style.color = "#95171B";
 	repque3.style.border = "1px solid #C8102E";
 	no3.style.visibility = "visible";
 }

 if(repque4.value===sol4.value){
 	repque4.style.color = "#0E5D24";
 	repque4.style.border = "1px solid #3CE68D";
 	resultat += 1;
 	yes4.style.visibility = "visible";
 	yes4.style.margin = "0px 0px 0px 20px";
 }else{
 	repque4.style.color = "#95171B";
 	repque4.style.border = "1px solid #C8102E";
 	no4.style.visibility = "visible";
 }

 if(repque5.value===sol5.value){
 	repque5.style.color = "#0E5D24";
 	repque5.style.border = "1px solid #3CE68D";
 	resultat += 1;
 	yes5.style.visibility = "visible";
 	yes5.style.margin = "0px 0px 0px 20px";
 }else{
 	repque5.style.color = "#95171B";
 	repque5.style.border = "1px solid #C8102E";
 	no5.style.visibility = "visible";
 }

 res.innerHTML = resultat+"/5 !";
 res.style.visibility = 'show';
 res.style.font = '24px;';
 res.style.float = 'left';
 res.style.margin = "0px 0px 0px 4px";
 bouton.style.margin= "0px 10px 8px 25px";

 if(resultat===0){
 	come.innerHTML = "C'est... Woaw, t'es un crack toi";
 }
 if(resultat===1){
 	come.innerHTML = "Essaie d'appuyer sur ALT et F4 pour voir ?";
 }
 if(resultat===2){
 	come.innerHTML = "2/5 en regardant sur Google ? Pas ouf.";
 }
 if(resultat===3){
 	come.innerHTML = "Bravo, tu dois surement battre ma grand-mere";
 }
 if(resultat===4){
 	come.innerHTML = "On dirait les profs de maths qui ne mettent jamais 20/20";
 }
  if(resultat===5){
 	come.innerHTML = "/gamemode 1";
 }
come.style.visibility = 'show';
come.style.font = "10px 'Noto Sans'";
bouton.style.float = 'left';

 bouton.innerHTML = "Recommencer";
 bouton.addEventListener("click",()=>{
        	location.href = "../jeu.py";
    	})
})



