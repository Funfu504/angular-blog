import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-authcallback',
  templateUrl: './auth-callback.component.html',
  styleUrls: ['./auth-callback.component.css']
})
export class AuthCallbackComponent {

constructor(private route: ActivatedRoute) {}

ngOnInit(): void {

  console.log('CALLBACK ORIGIN:', window.location.origin);
  console.log('CALLBACK PATH:', window.location.href);
  const code = this.route.snapshot.queryParamMap.get('code');

  console.log(code);
}

}
