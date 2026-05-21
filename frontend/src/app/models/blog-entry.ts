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
    summary: string;
    postDate : Date;
    featured : boolean;
}

export interface ICreateBlogEntry {
  "title": string,
  "summary": string,
  "blogText": string,
  "imageUrl": string,
  "imageAltText": string,
  "postDate": string,
  "featured": boolean,
  "authorId": string
}

export interface IUploadRequest {
  userId: string;
  filename: string;
  contentType: string;
}

export interface IUploadResponseDto {
  uploadUrl: string;
  fileKey: string;
}