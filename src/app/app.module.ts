import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { BlogEntryComponent } from './blog-entry/blog-entry.component';
import { BlogEntryPreviewComponent } from './blog-entry-preview/blog-entry-preview.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    BlogEntryComponent,
    BlogEntryPreviewComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
