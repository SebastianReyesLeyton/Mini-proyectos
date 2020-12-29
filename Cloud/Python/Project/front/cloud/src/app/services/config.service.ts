import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ConfigService {
  configUrl = 'http://127.0.0.1:32768';
  constructor( private http: HttpClient ) {  }

  getConfig(path: string): any {
    return this.http.get(`${this.configUrl}/files/${path}`);
  }

  uploadFile(path, file, name): any {
    let formData = new FormData();
    formData.append('file', file, name);
    console.log(`${this.configUrl}/saveFile/${path}`);
    return this.http.post(`${this.configUrl}/saveFile/${path}`, formData);
  }
}
