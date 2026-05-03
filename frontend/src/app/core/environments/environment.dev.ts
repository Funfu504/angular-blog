export const environment = {
  production: false,
  baseUrl: '__API_URL__' ,

  cognito: {
    userPoolId: 'us-east-1_6xapZLAa2',
    clientId: '7e0nn0g0t35if1q277rtasgq7j',
    domain: 'blog-dev-auth.auth.us-east-1.amazoncognito.com',

    redirectSignIn: [
      'https://d3ecwobg2ch99d.cloudfront.net/auth/callback'],

    redirectSignOut: [
      'https://d3ecwobg2ch99d.cloudfront.net']
  }
};