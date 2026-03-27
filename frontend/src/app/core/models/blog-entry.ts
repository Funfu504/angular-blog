export interface IBlogEntryDto {
  postId: string;
  title: string;
  summary: string;
  blogText: string;
  imageUrl: string;
  imageAltText: string;
  postDate: string;
  featured: string;
}

export interface IBlogEntry {
    postId : string;
    title : string;
    imageUrl : string;
    imageAltText : string;
    blogText : string;
    postDate : Date;
    featured : boolean;
}
