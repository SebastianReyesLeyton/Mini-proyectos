import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Data, user } from 'src/app/scripts/data';
import { ConfigService } from '../../services/config.service';

@Component({
  selector: 'app-files',
  templateUrl: './files.component.html',
  styleUrls: ['./files.component.css']
})
export class FilesComponent implements OnInit {
  info: Data;
  displayUrl = '';
  constructor( private configService: ConfigService ) { }

  getFiles(): void {
    this.configService
      .getConfig(`${user.username}${user.configUrl}/`)
      .subscribe((data: Data) => {
        console.log(data);
        this.info = data;
        if (user.configUrl !== '') {
          this.info.directories.unshift('/..');
        }
        console.log(this.info);
      });
    console.log('Esto se ejecutará antes que el console log de arriba');
  }

  getUpdir(folder: string): void {
    user.configUrl = `${user.configUrl}-${folder}`;
    if (this.displayUrl === '') {
      this.displayUrl = folder;
    }
    else {
      this.displayUrl = `${this.displayUrl}>${folder}`;
    }
    this.getFiles();
  }

  getDowndir(): void {
    let tmp: Array<string> = user.configUrl.split('-');
    tmp.pop();
    user.configUrl = tmp.join('-');
    tmp = this.displayUrl.split('>');
    tmp.pop();
    this.displayUrl = tmp.join('>');
    this.getFiles();
  }

  ngOnInit(): void {
    this.getFiles();
  }

}
