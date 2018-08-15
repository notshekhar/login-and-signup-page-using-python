
document.querySelector('#login').onclick = () => {
  let r = new XMLHttpRequest()
  r.open('POST', 'login')
  r.onloadstart = () => {
    console.log('loading')
  }
  r.onloadend = () => {
    let d = r.responseText
    d = JSON.parse(d)
    if(d.message=='yes'){
      console.log('welcome', d)
      cookie.setItem('uid', d.uid, 365)
      window.location = '/home'
      document.querySelector('#message').style.display = 'none'
    }else{
      document.querySelector('#message').style.display = 'block'
      document.querySelector('#message').innerText = d.message
    }

  }
  let data = new FormData()
  data.append("username", document.querySelector('#user').value)
  document.querySelector('#password').type = 'text'
  data.append("password", math.encode(document.querySelector('#password').value))
  document.querySelector('#password').type = 'password'
  r.send(data)
}
document.querySelector('#user').onkeyup = e =>{
  if(e.key == 'Enter'){
    document.querySelector('#password').focus()
  }
}
document.querySelector('#password').onkeyup = e =>{
  if(e.key == 'Enter'){
    document.querySelector('#login').click()
  }
}
document.querySelector('#signup').onclick = () => {
  let r = new XMLHttpRequest()
  r.open('POST', 'signup')
  r.onloadstart = () =>{
    console.log('loading')
  }
  r.onloadend = () => {
    let d = JSON.parse(r.responseText)
    if(d.message == 'yes'){
      console.log("welcome")
      cookie.setItem('uid', d.uid, 365)
      window.location = '/home'
      document.querySelector('#message').style.display = 'none'
    }else{
      document.querySelector('#message').style.display = 'block'
      document.querySelector('#message').innerText = d.message
    }
    console.log(d)
  }
  let data = new FormData()
  data.append('username', document.querySelector('#susername').value)
  document.querySelector('#spassword').type = 'text'
  data.append('password', math.encode(document.querySelector('#spassword').value))
  document.querySelector('#spassword').type = 'password'
  data.append('email', document.querySelector('#semail').value)
  r.send(data)
}
let createnewaccount = document.querySelector('#signu')
let loginuser = document.querySelector('#log')
let signup = document.querySelector('#sign')
let login = document.querySelector('#form')
createnewaccount.onclick = ()=>{
  login.style.display = 'none'
  signup.style.display = 'block'
}
loginuser.onclick = ()=>{
  login.style.display = 'block'
  signup.style.display = 'none'
}
document.querySelector('#susername').onkeyup = e =>{
  console.log(e.key)
  if(e.key == 'Enter'){
    document.querySelector('#spassword').focus()
  }
}
document.querySelector('#spassword').onkeyup = e =>{
  if(e.key == 'Enter'){
    document.querySelector('#semail').focus()
  }
}
document.querySelector('#semail').onkeyup = e =>{
  if(e.key == 'Enter'){
    document.querySelector('#signup').click()
  }
}
