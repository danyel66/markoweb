
var category = document.getElementsByName('category');

category[0].onclick = function() {

    category[0].firstElementChild.setAttribute("src", "/static/images/growth1.png");
    category[1].firstElementChild.setAttribute("src", "/static/images/cow1.png");
    category[2].firstElementChild.setAttribute("src", "/static/images/services-0.png");

    category[0].classList.add('active');
    category[1].classList.remove('active');
    category[2].classList.remove('active');

    var prodCate = document.querySelector(".product-category").style.left ="0";
}

category[1].onclick = function() {
    category[1].firstElementChild.setAttribute("src", "/static/images/cow2.png");
    category[0].firstElementChild.setAttribute("src", "/static/images/growth2.png");
    category[2].firstElementChild.setAttribute("src", "/static/images/services-0.png")

    category[1].classList.add('active');
    category[0].classList.remove('active');
    category[2].classList.remove('active');

    var prodCate = document.querySelector(".product-category").style.left ="-100%";

}

category[2].onclick = function() {
  category[2].firstElementChild.setAttribute("src", "/static/images/services-1.png")
  category[0].firstElementChild.setAttribute("src", "/static/images/growth2.png");
  category[1].firstElementChild.setAttribute("src", "/static/images/cow1.png");
  
  

  category[2].classList.add('active');
  category[0].classList.remove('active');
  category[1].classList.remove('active');

  var prodCate = document.querySelector(".product-category").style.left ="-200%";

}
