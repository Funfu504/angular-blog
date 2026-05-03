export const environment = {
  production: false,
  baseUrl: 'https://pytw9la54d.execute-api.us-east-1.amazonaws.com',
  
  cognito: {
    userPoolId: 'us-east-1_6xapZLAa2',
    clientId: '7e0nn0g0t35if1q277rtasgq7j',
    domain: 'blog-dev-auth.auth.us-east-1.amazoncognito.com',

    redirectSignIn: ['http://localhost:4200/auth/callback'],

    redirectSignOut: ['http://localhost:4200']
  }  
  
};