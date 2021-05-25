$(document).ready(function() {
	
	/* ======= Highlight.js Plugin ======= */ 
    /* Ref: https://highlightjs.org/usage/ */     
    $('pre code').each(function(i, block) {
	    hljs.highlightBlock(block);
	 });

});

const actidx = document.querySelector(".js-active__idx");

const actpost = document.querySelector(".js-active__post");

const actabt = document.querySelector(".js-active__about");

function setActiveIcon(){
    if (window.location.href == 'https://blog--lmknv.run.goorm.io/subinblog/'){
        actidx.classList.add("active");
        }
    else if (window.location.href == '/subinblog/post'){
        actpost.classList.add("active");
    }
    else if (window.location.href == 'subinblog/about'){
        actabt.classList.add("active");
    }
}