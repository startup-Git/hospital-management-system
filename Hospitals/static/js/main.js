// fixed-top
window.addEventListener("scroll", function () {
    let fixedNav = document.querySelector("header");
    if(window.pageYOffset > 0){
        fixedNav.classList.add("fixed-top");
    }else{
        fixedNav.classList.remove("fixed-top");
    }
});
// mobile toggle 
let mobile_toggle = document.getElementById("mobile_toggle");
mobile_toggle.addEventListener("click", toggle);
function toggle() {
    let x = document.getElementById("menu_bar");
    if (x.className === "menu_bar") {
        x.className += " toggle";    
    }else{
        x.className = "menu_bar";    
               
    }
}
// collapsible
let collapsible = document.getElementsByClassName('collapsible');
for (let index = 0; index < collapsible.length; index++) {
    collapsible[index].addEventListener('click',function(){
        this.classList.toggle('actives');
        var content = this.nextElementSibling;
        if(content.style.maxHeight){
            content.style.maxHeight = null;
        }else{
            content.style.maxHeight = content.scrollHeight += 'px';
        }
    });   
}
//counter value
const counters = document.querySelectorAll(".count");
  const speed = 400;

counters.forEach((counter) => {
  const updateCount = () => {
    const target = parseInt(+counter.getAttribute("data-target"));
    const count = parseInt(+counter.innerText);
    const increment = Math.trunc(target / speed);
    console.log(increment);

    if (count < target) {
      counter.innerText = count + increment;
      setTimeout(updateCount, 1);
    } else {
      count.innerText = target;
    }
  };
  let counterSection = document.querySelector(".counter_part_content");
  let Options = {
      rootMargin: '0px 0px -200px 0px' 
  }
  const sectioObserver = new IntersectionObserver(function(entries){
	  if(entries[0].isIntersecting){
        updateCount();
    }
  }, Options)
  sectioObserver.observe(counterSection);
});
//dependent selection system
let subjectObject = {
    'Dental': [
        'dr. jibon roy', 
        'harun', 
        'dr. jhotka', 
        'mainuddin', 
        'rashel khan',
        'ropiq hasan',
        'raju', 
        'mijaan ahmed'
    ],
    'medicine': [
        'anika akter',
        'raju', 
        'akash', 
        'dr. jhotka', 
        'delowar ali',
        'mijaan ahmed', 
        'mainuddin',
        'delowar ali'
    ],
    'Orthopedics': [
        'mainuddin',
        'parvez',
        'raju', 
        'akash', 
        'dr. jhotka', 
        'Neurosciences', 
        'harun'
    ],
    'Neurosciences': [
        'dr. jibon roy', 
        'raju', 
        'akash', 
        'dr. jhotka', 
        'kashem khan',
        'nur nobi',
        'dr. ali ahmmed'
    ],
    'Cancer care': [
        'dr. jhotka', 
        'dr. jibon roy', 
        'rashel khan',
        'akash', 
        'delowar ali',
        'raju', 
        'ar rone'
    ],
    'Gastroenterology': [ 
        'dr. jibon roy', 
        'rashel khan',
        'ropiq hasan',
        'raju', 
        'akash', 
        'dr. jhotka',
        'korim'
    ],
    'Familly Physicians': [ 
        'akash', 
        'dr. jhotka', 
        'dr. jibon roy', 
        'rashel khan',
        'ropiq hasan',
        'mijaan ahmed',
        'raju'
    ],
    
};
window.onload = function() {
    var DepartmentF = document.getElementById("validationCustom05 DepartmentF");
    var SpecialistF = document.getElementById("validationCustom06 SpecialistF");
    for (var x in subjectObject) {
        DepartmentF.options[DepartmentF.options.length] = new Option(x, x);
    }
    DepartmentF.onchange = function() {
      SpecialistF.length = 1;
      var select_option = subjectObject[this.value];
      while (SpecialistF.options.length > 0) {
        SpecialistF.options.remove(0);
      }
      Array.from(select_option).forEach(function(y){
        let option = new Option(y, y);
        SpecialistF.appendChild(option);
      });
    }

}

// // modal galery section
// var modal = document.getElementById("gis_Modal");
// var img = document.getElementById('gis_img');
// var modalImg = document.getElementById("mc_img");
// var captionText = document.getElementById("caption");
// var span = document.getElementsByClassName("close")[0];

// img.onclick = function(){
//   modal.style.display = "block";
//   modalImg.src = this.src;
//   captionText.innerHTML = this.alt;
// }
// img2.onclick = function(){
//     modal.style.display = "block";
//     modalImg.src = this.src;
//     captionText.innerHTML = this.alt;
// }
// img3.onclick = function(){
//     modal.style.display = "block";
//     modalImg.src = this.src;
//     captionText.innerHTML = this.alt;
// }
// img4.onclick = function(){
//     modal.style.display = "block";
//     modalImg.src = this.src;
//     captionText.innerHTML = this.alt;
// }
// img5.onclick = function(){
//     modal.style.display = "block";
//     modalImg.src = this.src;
//     captionText.innerHTML = this.alt;
// }
// img6.onclick = function(){
//     modal.style.display = "block";
//     modalImg.src = this.src;
//     captionText.innerHTML = this.alt;
// }
// img7.onclick = function(){
//     modal.style.display = "block";
//     modalImg.src = this.src;
//     captionText.innerHTML = this.alt;
// }
// img8.onclick = function(){
//     modal.style.display = "block";
//     modalImg.src = this.src;
//     captionText.innerHTML = this.alt;
// }
// span.onclick = function() { 
//   modal.style.display = "none";
// }
