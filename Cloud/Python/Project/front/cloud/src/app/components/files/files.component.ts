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
  configUrl = 'sebas.reyes';
  constructor( private configService: ConfigService ) { }

  getFiles(): void {
    this.configService
      .getConfig('sebas.reyes-Prueba/')
      .subscribe((data: Data) => {
        console.log(data);
        this.info = data;
        console.log(this.info);
      });
    console.log('Esto se ejecutará antes que el console log de arriba');
  }

  ngOnInit(): void {
    this.getFiles();
  }

}
