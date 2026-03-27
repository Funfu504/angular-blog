import { Injectable } from '@angular/core';
import { IBlogEntry, IBlogEntryDto } from '../models/blog-entry';
import { Observable, of, map } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BlogService {
  private apiUrl = 'http://127.0.0.1:8000'
  posts : IBlogEntry[] = [];
  
  constructor(private http: HttpClient) {    
    this.getPosts(10).subscribe(p => this.posts = p);    
  }

  getPosts(num_posts: number): Observable<IBlogEntry[]> {
     const theUrl = `${this.apiUrl}/posts?num_posts=${num_posts}&featured=false`
    return this.http.get<IBlogEntryDto[]>(theUrl)
      .pipe(map(dtos => dtos.map(this.mapBlogEntry)));
  }

  getPostById(id: string): Observable<IBlogEntry | undefined> {
    return of(this.posts.find(i => i.postId === id));
  }

  getLatestPost(): Observable<IBlogEntry | undefined> {
    return this.sortBlogPosts().pipe(
      map(items => items?.[0])
    );
  }

  /* example executing multiple maps on a dataset.
  getLatestPost(): Observable<IBlogEntry | undefined> {
    const url = "http://127.0.0.1:8000/posts?num_posts=2&featured=false"
    return this.http.get<IBlogEntryDto[]>(url)
      .pipe(map(dtos => dtos.map(this.mapBlogEntry)),map(posts => posts[0]));
  }
  */

  mapBlogEntry(dto: IBlogEntryDto): IBlogEntry {
    return {
      postId: dto.postId,
      title: dto.title,
      imageUrl: dto.imageUrl,
      imageAltText: dto.imageAltText,
      blogText: dto.blogText,
      postDate: new Date(dto.postDate),
      featured: dto.featured === '1'
    };
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
        postId: "1",
        title: "My First Blog Post",
        imageUrl: "/assets/images/FeelsTheCat.jpg",
        imageAltText: "Feels The Cat",
        blogText: "Wall of Text",
        postDate: new Date(2026, 1, 31),
        featured: false},
      {
        postId: "2",
        title: "Learning Python",
        imageUrl: "/assets/images/PythonLogo.png",
        imageAltText: "Official Python Logo",
        blogText: "Wall of Text",
        postDate: new Date(2026, 1, 30),
        featured: true
      },
      {
        postId: "3",
        title: "Learning Angular",
        imageUrl: "/assets/images/AngularLogo.png",
        imageAltText: "Angular Logo",
        blogText: "Wall of Text",
        postDate: new Date(2026, 1, 29),
        featured: true
      },
      {
        postId: "4",
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
