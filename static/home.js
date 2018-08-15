document.querySelector('#logout').onclick = () =>{
  cookie.setItem('uid', null, 365)
  window.location = '/'
}
