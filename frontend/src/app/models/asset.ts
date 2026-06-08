export interface IUploadRequest {
  userId: string;
  filename: string;
  contentType: string;
}

export interface IUploadResponseDto {
  uploadUrl: string;
  fileKey: string;
}