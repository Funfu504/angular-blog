import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { BlogEntryComponent } from './pages/blog-entry/blog-entry.component';
import { BlogEntryPreviewComponent } from './pages/blog-entry-preview/blog-entry-preview.component';
import { SiteHeaderComponent } from './pages/site-header/site-header.component';
import { AppRoutingModule } from './app-routing.module';
import { AboutComponent } from './pages/about/about.component';
import { CallbackComponent } from './pages/auth/callback/callback.component';
import { AuthcallbackComponent } from './pages/auth/auth-callback.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    BlogEntryComponent,
    BlogEntryPreviewComponent,
    SiteHeaderComponent,
    AboutComponent,
    CallbackComponent,
    AuthcallbackComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
