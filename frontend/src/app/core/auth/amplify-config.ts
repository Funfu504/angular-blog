import { Amplify } from 'aws-amplify';

import { environment } from '../environments/environment';

export function initAmplify() {
    console.log("AMPLIFY INIT CALLED");
    Amplify.configure({
    Auth: {
        Cognito: {
            userPoolId: environment.cognito.userPoolId,
            userPoolClientId: environment.cognito.clientId,

            loginWith: {
                oauth: {
                domain: environment.cognito.domain,

                scopes: [
                    'openid',
                    'email',
                    'profile'
                ],

                redirectSignIn: environment.cognito.redirectSignIn,

                redirectSignOut: environment.cognito.redirectSignOut,

                responseType: 'code'
                }
            }
        }
    }
    });
}