import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ApiService } from 'src/app/services/api.service';
import { JwtService } from 'src/app/services/jwt.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginForm: FormGroup;
  eyeIconPath: string = '../../../../assets/icons/eye.svg';
  eyeIconVisiblePath: string = '../../../../assets/icons/no-eye.svg';
  showPassword: boolean = false;
  eyeIcon: string = this.eyeIconPath;

  constructor(
    private fb: FormBuilder,
    private apiService: ApiService,
    private jwtService: JwtService,
    private router: Router
  ) {
    this.loginForm = this.fb.group({
      user: ['', [Validators.required, Validators.minLength(6), Validators.maxLength(10)]],
      password: ['', [Validators.required, Validators.minLength(4), Validators.maxLength(8)]]
    });
  }

  ngOnInit(): void {}

  onSubmit(): void {
    if (this.loginForm.valid) {
      const userLogin = this.loginForm.value;

      this.apiService.postData('login', userLogin).subscribe(
        (response) => {
          this.jwtService.setToken(response.token);
          this.router.navigate(['/home']);
        },
        (error) => {
          if (error.status === 404) {
            window.alert("Usuario o contraseña incorrectos.");
          } else {
            window.alert("Ha ocurrido un error inesperado, por favor intenta de nuevo.");
          }
          console.log(error);
        }
      );
    } else {
      this.loginForm.markAllAsTouched();
    }
  }

  togglePasswordVisibility(): void {
    this.showPassword = !this.showPassword;
    const passwordInput = document.getElementById('password') as HTMLInputElement;
    passwordInput.type = this.showPassword ? 'text' : 'password';
    this.eyeIcon = this.showPassword ? this.eyeIconVisiblePath : this.eyeIconPath;
  }
}
