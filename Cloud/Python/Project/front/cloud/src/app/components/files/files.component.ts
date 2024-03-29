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

  deleteFile(name): void {
    this.configService
      .deleteFile(`${user.username}${user.configUrl}`, name)
      .subscribe((res) => {
        console.log(res);
        location.reload();
      });
  }

  getFile(name): void {
    let route = `${user.username}${user.configUrl}-${name}`;
    this.configService.getFile(route)
      .subscribe((res) => {
        console.log(res);
        const a = document.createElement('a');
        const objectUrl = URL.createObjectURL(res);
        a.href = objectUrl;
        a.download = name;
        a.click();
        URL.revokeObjectURL(objectUrl);
      });
  }

  ngOnInit(): void {
    this.getFiles();
  }

}
