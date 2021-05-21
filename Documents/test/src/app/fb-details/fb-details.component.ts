import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Fb } from '../fb';
import { MembreService } from '../membre.service';

@Component({
  selector: 'fb-details',
  templateUrl: './fb-details.component.html',
  styleUrls: ['./fb-details.component.scss']
})

export class FbDetailsComponent implements OnInit {

  @Input() id: number;
  fb: Fb;

  constructor(private membreService: MembreService) { }

  ngOnInit(): void {
    this.reloadData();
  }

  reloadData(){
    this.membreService.getFbById(this.id).subscribe(
      data => {
        this.fb = data;
      }
    );
  }

}
