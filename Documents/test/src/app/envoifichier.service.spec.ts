import { TestBed } from '@angular/core/testing';

import { EnvoifichierService } from './envoifichier.service';

describe('EnvoifichierService', () => {
  let service: EnvoifichierService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EnvoifichierService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
