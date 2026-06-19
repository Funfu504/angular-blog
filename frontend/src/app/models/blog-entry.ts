export interface IBlogEntryDto {
  postId: string;
  title: string;
  summary: string;
  blogText: string;
  imageUrl: string;
  imageAltText: string;
  postDate: string;
  featured: boolean;
}

export interface IBlogEntry {
    postId : string;
    title : string;
    imageUrl : string;
    imageAltText : string;
    blogText : string;
    summary: string;
    postDate : Date;
    featured : boolean;
}

export interface ICreateBlogEntry {
  "title": string,
  "summary": string,
  "blogText": string,
  "imageFileName": string,
  "imageUrl": string,
  "imageAltText": string,
  "postDate": string,
  "featured": boolean,
  "authorId": string
}