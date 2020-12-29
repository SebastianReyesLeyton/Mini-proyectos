import { Component, OnInit } from '@angular/core';
import { user } from '../../scripts/data';
import { ConfigService } from '../../services/config.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-options',
  templateUrl: './options.component.html',
  styleUrls: ['./options.component.css']
})
export class OptionsComponent implements OnInit {
  user;
  files: File;

  constructor(private configService: ConfigService) {
  }

  ngOnInit(): void {
  }

  uploadFile(): void {
    console.log(this.files);
    this.configService
      .uploadFile(`${user.username}${user.configUrl}/`, this.files, this.files.name)
      .subscribe((res) => {
        console.log(res);
        location.reload();
      });
  }

  storeFiles(e): void {
    console.log(e);
    this.files = e.target.files[0];
  }
}
