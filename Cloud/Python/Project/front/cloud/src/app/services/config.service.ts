import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ConfigService {
  configUrl = 'http://192.168.1.8:32768';
  constructor( private http: HttpClient ) {  }

  modifyNameFile(name): string {
    return name.split('-').join('_');
  }

  getConfig(path: string): any {
    return this.http.get(`${this.configUrl}/files/${path}`);
  }

  uploadFile(path, file, name): any {
    let formData = new FormData();
    formData.append('file', file, this.modifyNameFile(name));
    console.log(`${this.configUrl}/saveFile/${path}`);
    return this.http.post(`${this.configUrl}/saveFile/${path}`, formData);
  }

  deleteFile(path, name): any {
    return this.http.post(`${this.configUrl}/removeFile/${path}`, {filename: name});
  }

  getFile(path): any {
    return this.http.get(`${this.configUrl}/readFile/${path}`, {responseType: 'blob'});
  }
}
