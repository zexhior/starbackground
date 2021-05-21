import { Component, OnInit } from '@angular/core';
import { EnvoifichierService } from '../envoifichier.service';

@Component({
  selector: 'app-upload-file',
  templateUrl: './upload-file.component.html',
  styleUrls: ['./upload-file.component.scss']
})
export class UploadFileComponent implements OnInit {

  fichierAEnvoyer: File = null;

  constructor(private envoirFichier: EnvoifichierService) { }

  ngOnInit(): void {
  }

  envoiFichier(fichiers: FileList){
    this.fichierAEnvoyer = fichiers.item[0];
  }

  envoiFichierParLeService(){
    
  }

}
