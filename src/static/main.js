document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
  });


document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems, {});
  });

document.addEventListener('DOMContentLoaded', function() {
var elems = document.querySelectorAll('.sidenav');
var instances = M.Sidenav.init(elems, {});
});

let yr = document.querySelector('.my-date')
let currentTIme = new Date()
let text = document.createTextNode(`${currentTIme.getFullYear()} @ njorogetimk`)
yr.appendChild(text)

