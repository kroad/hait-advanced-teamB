<template>
  <div>
    <v-container>
      <v-card>
        <v-tabs v-model="tab" background-color="transparent" color="basil" grow>
          <v-tab v-for="item in items" :key="item">
            {{ item }}
          </v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab">
          <v-tab-item>
            <v-card>
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      v-model="loginForm.username"
                      :rules="[rules.required]"
                      label="ユーザー名"
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
                      :rules="[rules.required, rules.min]"
                      :type="show3 ? 'text' : 'password'"
                      label="パスワード"
                      hint="At least 8 characters"
                      v-model="loginForm.password"
                      @click:append="show3 = !show3"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-btn @click="submitLogin"> ログイン </v-btn>
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-tab-item>
          <v-tab-item>
            <v-card>
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      v-model="registerForm.username"
                      :rules="[rules.required]"
                      label="ユーザー名"
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
                      :rules="[rules.required, rules.min]"
                      :type="show3 ? 'text' : 'password'"
                      label="パスワード"
                      hint="At least 8 characters"
                      v-model="registerForm.password1"
                      @click:append="show3 = !show3"
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
                      :rules="[rules.required, rules.emailMatch]"
                      :type="show3 ? 'text' : 'password'"
                      label="再入力"
                      hint="confirm the password"
                      v-model="registerForm.password2"
                      @click:append="show3 = !show3"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-btn color="primary" @click="submitRegister">
                      新規登録
                    </v-btn>
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-tab-item>
        </v-tabs-items>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loginForm: {
        username: "",
        password: "",
      },
      registerForm: {
        username: "",
        password1: "",
        password2: "",
      },
      show3: false,
      rules: {
        required: (value) => !!value || "Required.",
        min: (v) => v.length >= 8 || "Min 8 characters",
        emailMatch: (v) =>
          v === this.registerForm.password1 || `パスワードが一致しません`,
      },
      tab: null,
      items: ["ログイン", "新規登録"],
    };
  },
  methods: {
    // ログインボタン押下
    submitLogin: function () {
      // ログイン
      this.$store
        .dispatch("auth/login", {
          username: this.loginForm.username,
          password: this.loginForm.password,
        })
        .then(() => {
          console.log("Login succeeded.");
          this.$store.dispatch("message/setInfoMessage", {
            message: "ログインしました。",
          });
          // クエリ文字列に「next」がなければ、ホーム画面へ
          const next = this.$route.query.next || "/";
          this.$router.replace(next);
        });
    },
    // 新規登録ボタン押下
    submitRegister: function () {
      // 新規登録
      this.$store
        .dispatch("auth/register", {
          username: this.registerForm.username,
          password1: this.registerForm.password1,
          password2: this.registerForm.password2,
        })
        .then(() => {
          console.log("Register succeeded.");
          this.$store.dispatch("message/setInfoMessage", {
            message: "新規登録しました。",
          });
          // クエリ文字列に「next」がなければ、ホーム画面へ
          const next = this.$route.query.next || "/";
          this.$router.replace(next);
        });
    },
  },
};
</script>