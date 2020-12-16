import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Data } from 'src/app/scripts/data';
import { ConfigService } from '../../services/config.service';

@Component({
  selector: 'app-files',
  templateUrl: './files.component.html',
  styleUrls: ['./files.component.css']
})
export class FilesComponent implements OnInit {
  info: Data;
  user = 'sebas.reyes';
  configUrl = '';
  displayUrl = '';
  constructor( private configService: ConfigService ) { }

  getFiles(): void {
    this.configService
      .getConfig(`sebas.reyes${this.configUrl}/`)
      .subscribe((data: Data) => {
        console.log(data);
        this.info = data;
        if (this.configUrl !== '') {
          this.info.directories.unshift('/..');
        }
        console.log(this.info);
      });
    console.log('Esto se ejecutará antes que el console log de arriba');
  }

  getUpdir(folder: string): void {
    this.configUrl = `${this.configUrl}-${folder}`;
    if (this.displayUrl === '') {
      this.displayUrl = folder;
    }
    else {
      this.displayUrl = `${this.displayUrl}>${folder}`;
    }
    this.getFiles();
  }

  getDowndir(): void {
    let tmp: Array<string> = this.configUrl.split('-');
    tmp.pop();
    this.configUrl = tmp.join('-');
    tmp = this.displayUrl.split('>');
    tmp.pop();
    this.displayUrl = tmp.join('>');
    this.getFiles();
  }

  ngOnInit(): void {
    this.getFiles();
  }

}
