import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AboutComponent } from './pages/about/about.component';
import { AuthCallbackComponent } from 'src/core/auth/pages/callback/auth-callback.component';

const routes: Routes = [
  {path: "home", component: HomeComponent, title: "Home - Moe's Blog"},
  {path: "about", component: AboutComponent, title: "About - Moe's Blog"},
  {path: "auth/callback", component: AuthCallbackComponent}
  ];

@NgModule({
  declarations: [],
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }
