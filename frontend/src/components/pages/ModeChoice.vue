<template>
  <div>
    <v-container>
      <v-row>
        <v-col>
          <v-card dark>
            <v-card-title>測定</v-card-title>
            <v-card-subtitle>モードを選んでください</v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>
      <v-card dark to="/measure/myvoice">
        <v-card-title> マイVOICEを使う</v-card-title>
        <v-card-subtitle> 測定は１回で終わります</v-card-subtitle>
      </v-card>
      <v-card dark to="/measure/select">
        <v-card-title>最高音・最低音は選択 </v-card-title>
        <v-card-subtitle>
          スピーカーから出る音で音程をチェックします。測定は一回で終わります
        </v-card-subtitle>
      </v-card>
      <v-card dark to="/measure/record">
        <v-card-title> 最高音・最低音もマイクで測定 </v-card-title>
        <v-card-subtitle> 測定は3回します </v-card-subtitle>
      </v-card>
    </v-container>
  </div>
</template>
<script>
export default {};
</script>