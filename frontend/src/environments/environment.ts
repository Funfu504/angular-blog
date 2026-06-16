export const environment = {
  production: false,
  baseUrl: 'http://127.0.0.1:8000',
  
  cognito: {
    userPoolId: 'us-east-1_6xapZLAa2',
    clientId: '7e0nn0g0t35if1q277rtasgq7j',
    domain: 'blog-dev-auth.auth.us-east-1.amazoncognito.com',

    redirectSignIn: ['http://localhost:4200/auth/callback'],

    redirectSignOut: ['http://localhost:4200'],
  },
  
  cdn: {
    baseUrl: 'http://localhost:9000/angular-blog-dev-assets/',
  }
  
};