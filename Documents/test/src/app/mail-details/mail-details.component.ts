import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Mail } from '../mail';
import { MembreService } from '../membre.service';

@Component({
  selector: 'mail-details',
  templateUrl: './mail-details.component.html',
  styleUrls: ['./mail-details.component.scss']
})
export class MailDetailsComponent implements OnInit {
  
  @Input() id: number;
  mail: Mail;

  constructor(private membreService: MembreService) { }

  ngOnInit(): void {
    this.reloadData();
  }

  reloadData(){
    this.membreService.getMailById(this.id).subscribe(
      data => {
        this.mail = data;
      }
    );
  }

}
