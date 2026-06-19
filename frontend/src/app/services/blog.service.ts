import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of, map, switchMap, tap } from 'rxjs';
import { IBlogEntry, IBlogEntryDto, ICreateBlogEntry } from '../models/blog-entry';
import { IUploadRequest, IUploadResponseDto } from '../models/asset';
import { environment } from "src/environments/environment"
import { ApiPaths } from "../enums/api-paths"

@Injectable({
  providedIn: 'root'
})
export class BlogService {
  posts : IBlogEntry[] = [];
  
  constructor(private http: HttpClient) {    
    //this.getPosts(10).subscribe(p => this.posts = p);    
  }

  getPosts(num_posts: number): Observable<IBlogEntry[]> {
    
    //debugger;
    
    if (this.posts && this.posts.length > 0)
    {      
      return of(this.posts);
    }
    else
    {    
      const theUrl = `${environment.baseUrl}${ApiPaths.Posts}?num_posts=${num_posts}&featured=false`

      return this.http.get<IBlogEntryDto[]>(theUrl)
        .pipe(
          map(dtos => dtos.map(this.mapBlogEntry)), 
          tap((posts) => this.posts = posts)
        );
    }
  }

  getPostById(id: string): Observable<IBlogEntry | undefined> {
    return this.getPosts(10).pipe(
      map(getPostResponse => getPostResponse?.find(i => i.postId === id))      
    );
  }

  /*
  getPostById(id: string): Observable<IBlogEntry | undefined> {
    return of(this.posts.find(i => i.postId === id));
  }
  */

  getLatestPost(): Observable<IBlogEntry | undefined> {
    return this.sortBlogPosts().pipe(
      map(items => items?.[0])
    );
  }

  mapBlogEntry(dto: IBlogEntryDto): IBlogEntry { 
    return {
      postId: dto.postId,
      title: dto.title,
      imageUrl: `${environment.cdn.baseUrl}${dto.imageUrl}`,
      imageAltText: dto.imageAltText,
      blogText: dto.blogText,
      summary: dto.summary,
      postDate: new Date(dto.postDate),
      featured: dto.featured
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
    return this.getPosts(10).pipe(
      map(getPostResponse => getPostResponse.sort((a, b) => b.postDate.getTime() - a.postDate.getTime()))
    )
  }

  /*
  sortBlogPosts(): Observable<IBlogEntry[] | undefined> {
    return of(this.posts.sort((a, b) => b.postDate.getTime() - a.postDate.getTime()))
  }*/

  createBlogPost(post: ICreateBlogEntry, file: FormData): Observable<IBlogEntry | undefined> {
    
    const theGenImageUploadUrl = `${environment.baseUrl}${ApiPaths.GenUploadUrl}`    

    const imageRequest: IUploadRequest = {
      "userId": "Moe",
      "filename": (file.get("fileName") as string),
      "contentType": (file.get("contentType") as string)
    }

    //first generate the S3 upload url
    return this.http.post<IUploadResponseDto>(theGenImageUploadUrl, imageRequest)
    .pipe( //next post the image to S3.
      switchMap((genUrlUploadResponse) => this.uploadAsset(genUrlUploadResponse, post, file)),      
      switchMap(() => this.createPost(post)), //finally save the post to the backend.
      tap(() => this.posts = [])
    )
  }

  private uploadAsset(genUrlUploadResponse: IUploadResponseDto, post: ICreateBlogEntry, file: FormData)
  {
    post.imageUrl = genUrlUploadResponse.fileKey
    post.imageFileName = genUrlUploadResponse.fileName
    return this.http.put(
      genUrlUploadResponse.uploadUrl, 
      file.get("thumbnail"), 
      {
        headers: {
          'Content-Type': (file.get("contentType") as string)
        }
      })
  }

  private createPost(post: ICreateBlogEntry): Observable<IBlogEntry>
  {
    const theCreatePostUrl = `${environment.baseUrl}${ApiPaths.CreatePost}`

    console.log("Final DB Update")
    console.log("THE URL", theCreatePostUrl)
    console.log("THE CONTENT", post)
    return this.http.post<IBlogEntryDto>(theCreatePostUrl, post)
    .pipe(map(dto => this.mapBlogEntry(dto)))
  }

  getBlogEntryList(){
    this.posts = [
      {
        postId: "1",
        title: "My First Blog Post",
        imageUrl: "/assets/images/FeelsTheCat.jpg",
        imageAltText: "Feels The Cat",
        blogText: "Wall of Text",
        summary: "summary",
        postDate: new Date(2026, 1, 31),
        featured: false},
      {
        postId: "2",
        title: "Learning Python",
        imageUrl: "/assets/images/PythonLogo.png",
        imageAltText: "Official Python Logo",
        blogText: "Wall of Text",
        summary: "summary",        
        postDate: new Date(2026, 1, 30),
        featured: true
      },
      {
        postId: "3",
        title: "Learning Angular",
        imageUrl: "/assets/images/AngularLogo.png",
        imageAltText: "Angular Logo",
        blogText: "Wall of Text",
        summary: "summary",        
        postDate: new Date(2026, 1, 29),
        featured: true
      },
      {
        postId: "4",
        title: "About Me",
        imageUrl: "",
        imageAltText: "none",
        blogText: "I am the owner of this blog.",
        summary: "summary",
        postDate: new Date(2026, 1, 1),
        featured: false
      }      
    ]
  }
}
