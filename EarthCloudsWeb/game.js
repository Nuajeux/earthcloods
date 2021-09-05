 const repque1 = document.querySelector("#qu1");

 const sol1 = document.querySelector("#solu1");
console.log('coucou');

const bouton = document.querySelector("button");

bouton.addEventListener("click",()=>{
 if(repque1.value===sol1.value){
 	repque1.style.width = "200px";
 	console.log('oui');
 }
})


