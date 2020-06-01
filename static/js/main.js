// const signUpButton = document.getElementById('signUp');
// const signInButton = document.getElementById('signIn');
// const container = document.getElementById('container');

// signUpButton.addEventListener('click', () => {
// 	container.classList.add("right-panel-active");
// });

// signInButton.addEventListener('click', () => {
// 	container.classList.remove("right-panel-active");
// });

// document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.parallax');
//     var instances = M.Parallax.init(elems, options);
//   });

  // Or with jQuery

  // $(document).ready(function(){
  //   $('.parallax').parallax();
  // });
  // var instance = M.Parallax.getInstance(elem);
  $(".dropdown-trigger").dropdown();
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.parallax');
    var instance = M.Parallax.getInstance(elems);
    $(".dropdown-trigger").dropdown();
  });



  // Or with jQuery

 