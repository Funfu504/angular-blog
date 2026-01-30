import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { BlogEntryComponent } from './pages/blog-entry/blog-entry.component';

const routes: Routes = [
  {path: "home", component: HomeComponent, title: "Home - Moe's Blog"},
  {path: "about", component: BlogEntryComponent, title: "About - Moe's Blog"}
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
