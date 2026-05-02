import { Injectable } from '@angular/core';
import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { Observable, from } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { fetchAuthSession } from 'aws-amplify/auth';
import { environment } from '../environments/environment';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    
    console.log('INTERCEPTOR HIT');
    console.log(req.url);
    
    /*
      Only attach token to YOUR backend API calls.
      Skip external URLs.
    
    if (!req.url.startsWith(environment.baseUrl)) {
      return next.handle(req);
    }*/

    /*
      fetchAuthSession() is async, so we convert
      the Promise into an Observable with from().
    */
    return from(fetchAuthSession()).pipe(

      switchMap((session) => {

        /*
          For API Gateway JWT authorizers,
          accessToken is commonly used.
        */
        const token =
          session.tokens?.accessToken?.toString();
console.log(token);
        /*
          If no token exists,
          just continue request unchanged.
        */
        if (!token) {
          return next.handle(req);
        }

        /*
          Requests are immutable in Angular.
          Clone request and add Authorization header.
        */
        const authReq = req.clone({

          setHeaders: {
            Authorization: `Bearer ${token}`
          }

        });

        return next.handle(authReq);

      })

    );

  }

}