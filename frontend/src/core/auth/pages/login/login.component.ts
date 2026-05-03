import { Component } from '@angular/core';
import { signInWithRedirect } from 'aws-amplify/auth';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  login()
  {    
    console.log('LOGIN ORIGIN:', window.location.origin);
    console.log('LOGIN PATH:', window.location.href);
    signInWithRedirect();
  }
}