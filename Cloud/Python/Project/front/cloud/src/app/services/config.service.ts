import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { Data } from 'src/app/scripts/data';

@Injectable({
  providedIn: 'root'
})
export class ConfigService {
  configUrl = 'http://127.0.0.1:32776/files';
  constructor( private http: HttpClient ) {  }

  configUrl1 = 'assets/config.json';

  getConfig(path: string): any {
    return this.http.get(`${this.configUrl}/${path}`);
  }

}
