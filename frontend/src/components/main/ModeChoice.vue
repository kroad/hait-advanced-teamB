<template>
  <div>
    <v-container>
      <v-row>
        <v-col>
          <v-card>
            <v-card-title>測定</v-card-title>
            <v-card-subtitle>モードを選んでください</v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>
      <v-card to="/measure/myvoice">
        <v-card-title> マイVOICEを使う</v-card-title>
        <v-card-subtitle> 測定は１回で終わります</v-card-subtitle>
      </v-card>
      <v-card to="/measure/select">
        <v-card-title>最高音・最低音は選択 </v-card-title>
        <v-card-subtitle>
          スピーカーから音が出ます.測定は一回で終わります
        </v-card-subtitle>
      </v-card>
      <v-card to="/measure/record">
        <v-card-title> 最高音・最低音もマイクで測定 </v-card-title>
        <v-card-subtitle> 音程をリアルタイムで表示します </v-card-subtitle>
      </v-card>
    </v-container>
  </div>
</template>
<script>
export default {};
</script>