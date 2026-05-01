import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor() { }
 
  login(): void {

  const clientId = 'YOUR_CLIENT_ID';

  const redirectUri =
    encodeURIComponent('http://localhost:4200/auth/callback');

  const domain =
    'https://blog-dev-auth.auth.us-east-1.amazoncognito.com';

  window.location.href =
    `${domain}/login` +
    `?client_id=${clientId}` +
    `&response_type=code` +
    `&scope=openid+email+profile` +
    `&redirect_uri=${redirectUri}`;
}
}
