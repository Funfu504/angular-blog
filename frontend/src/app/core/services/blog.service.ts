import { Injectable } from '@angular/core';
import { IBlogEntry } from '../models/blog-entry';
import { Observable, of, map } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BlogService {
  posts : IBlogEntry[] = [];

  constructor() { 
    this.getBlogEntryList();
  }

  getPosts(): Observable<IBlogEntry[]> {
    return of(this.posts);
  }

  getPostById(id: number): Observable<IBlogEntry | undefined> {
    return of(this.posts.find(i => i.id === id));
  }

  getLatestPost(): Observable<IBlogEntry | undefined> {
    return this.sortBlogPosts().pipe(
      map(items => items?.[0])
    );
  }

  //the About Me Post is going to be the FIRST post into the system...this will eventually be a problem.
  //for now it's fine, but eventually we'll just put it in as a special Type and just fetch that one.
  getAboutMePost(): Observable<IBlogEntry | undefined> {
    return this.sortBlogPosts().pipe(
      map(items => items?.[items.length-1])
    )
  }

  getFeaturedPosts(max : number): Observable<IBlogEntry[] | undefined> {
    return this.sortBlogPosts().pipe(
      map(items => items?.filter(items => items.featured === true).slice(0,max))
    )
  }

  sortBlogPosts(): Observable<IBlogEntry[] | undefined> {
    return of(this.posts.sort((a, b) => b.postDate.getTime() - a.postDate.getTime()))
  }

  getBlogEntryList(){
    this.posts = [
      {
        id: 1,
        title: "My First Blog Post",
        imageUrl: "/assets/images/FeelsTheCat.jpg",
        imageAltText: "Feels The Cat",
        blogText: "Wall of Text",
        postDate: new Date(2026, 1, 31),
        featured: false},
      {
        id: 2,
        title: "Learning Python",
        imageUrl: "/assets/images/PythonLogo.png",
        imageAltText: "Official Python Logo",
        blogText: "Wall of Text",
        postDate: new Date(2026, 1, 30),
        featured: true
      },
      {
        id: 3,
        title: "Learning Angular",
        imageUrl: "/assets/images/AngularLogo.png",
        imageAltText: "Angular Logo",
        blogText: "Wall of Text",
        postDate: new Date(2026, 1, 29),
        featured: true
      },
      {
        id: 4,
        title: "About Me",
        imageUrl: "",
        imageAltText: "none",
        blogText: "I am the owner of this blog.",
        postDate: new Date(2026, 1, 1),
        featured: false
      }      
    ]
  }
}
