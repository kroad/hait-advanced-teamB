<template>
  <div>
    <v-container>
      <v-card>
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="form.username"
                label="ユーザー名"
                outlined
              ></v-text-field>
            </v-col>

            <v-col cols="12">
              <v-text-field
                v-model="form.password"
                label="パスワード"
                outlined
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
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    // ログインボタン押下
    submitLogin: function () {
      // ログイン
      this.$store
        .dispatch("auth/login", {
          username: this.form.username,
          password: this.form.password,
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
  },
};
</script>