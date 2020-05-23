# -*- coding: utf-8 -*-
import sys
d1 = []
d2 = []
Correctlist = {':flag_jp:': ':flag_cn:', 'アメリカ': '美国', 'ラーメン': 'うーメソ', '為': '为', 'HUAWEI': '华为技术有限公司', 'Huawei': '华为技术有限公司', 'ファーウェイ': '华为技术有限公司', 'スペック': 'ﾇﾍﾟｯｹ', 'グ': 'ゲ', '国': '國', 'し': 'レ', '偽': '伪', '雑': '杂', '貨': '货', '書': '畫', 'る': 'ゑ', 'う': 'ラ', 'ス': 'ヌ', '語': '语', 'く': 'ㄑ', '貴': '贵', '様': '樣', '応': '应', '見': '见', 'ン': 'ソ', 'ね': 'れ', '魚': '鱼', 'シ': 'ツ゚', 'ル': '儿', 'オ': '才', '勝': '胜', 'HONOR': '荣耀', 'Honor': '荣耀', 'Google': '谷歌', '綺': '绮', 'Balong': '巴龙', 'Ascend': '昇騰', 'Kunpeng': '鯤鵬', '麗': '丽', 'あなた': '贵樣', '贵方': '贵樣', 'お前': '贵樣', 'あんた': '贵樣', '恋': '戀', 'ヨ': '彐', 'ョ': '彐', '浜': '滨', '濱': '滨', '濵': '滨', '沢': '泽', '澤': '泽', '私': '仆', 'あたし': '仆', 'わたし': '仆', 'わたくし': '仆', '当': '當', 'で': 'て', '額': '额', 'す': 'ず', '尋': '寻', '湯': '汤', '00円': '00日元', 'の': 'ゐ', 'リ': '刂', 'り': 'リ', 'ズ': 'ス', 'ッ': 'シ', '続': '续', '気': '气', 'ボ': '㝳', '購': '购', '買': '买', 'ベ': 'へ', '許': '许', '絵': '绘', '長': '长', '覚': '覺', '錯': '错', '開': '开', '評': '评', '華': '华', '約': '约', '預': '预', '乾燥': '极度干燥', '間': '间', '飛': '飞', '時': '时', '伝': '传', 'テ': '亍', 'ジ': 'ヅ', '頼': '赖', '結': '结', '論': '论', '悪': '恶', 'ゼ': '乜"', 'セ': '乜', '話': '话', '電': '电', '状': '狀', '険': '險', '財': '财', '声': '聲', '動': '动', 'メ': '〆', '変': '变', '記': '记', '号': '號', '監': '监', '韓': '韩', '簡': '简', '較': '较', '顔': '颜', '愛': '爱', '違': '违', '総': '總', '届': '屆', '学': '學', '獣': '獸', '岡': '冈', '輩': '辈', '親': '亲', '乗': '乘', 'ハ': '八', 'ミ': 'シ', 'ク': 'ケ', 'なさい': '\(しなさい\)', '会': '會', 'ア': 'マ', '楽': '乐', '偉': '伟', 'パ': '八゜', '際': '际', '揮': '毫', '来': '來', 'ペ': 'へ', 'エ': '卫', 'ェ': '卫', '労働': '極度勞動（しなさい\）', '風': '风', '東': '东', '経': '经', '両': '两', '拡': '扩', '戦': '战', '務': '务', 'カ': '力', 'か': 'カ', '夢': '梦', '調': '调', 'Amazon': '亚马逊', '潰': '溃', '選': '选', '関': '关', '値': '價', '義': '义', '体': '體', '黒': '黑', '須': '须', '報': '报', '想像': '極度想像（しなさい\）', '強': '强', '確': '确', '税': '稅', '軽': '轻', 'ヒ': '匕', '編': '编', 'それ': 'そね', '対': '对', '殺': '杀', '進': '进', '飲': '饮', '議': '议', '壊': '坏', 'Yahoo! News': 'カフー二ューヌ', '偵': '侦', 'コナソ': 'ゴメソ', '協': '协', '温': '溫', '厳': '嚴', '遊': '游', '黄': '黃', '僕': '仆', '純': '纯', '習': '习', '緒': '绪', '潤': '润', '質': '质', '証': '證', '内': '內', '焼': '燒', '軍': '军', '艦': '舰', '勧': '勸', '売': '卖', '増': '增', '員': '员', ':crossed_flags:': ':flag_cn:', ':flag_au:': ':flag_cn:', ':flag_kr:': ':flag_cn:', '島': '岛', '熱': '热', '歴': '历', '満': '满', '統': '统', '銀': '银', '綾': '绫', '団': '团', '過': '过', '読': '读', '癒': '愈', '覧': '览', '前代未聞': '前所未有', '知恵': '智慧', 'Da Zhang Wei': '大张伟', 'Da ZhangWei': '大张伟', 'Da Zhangwei': '大张伟', 'Wowkie Zhang': 'Da Zhang Wei', '人间精品': '人间精品起來嗨', '飯': '饭', 'Xperia': 'Huawei', 'AQUOS': 'HUAWEI', '終': '终', 'TBS': 'CCTV', '縦': '纵', '大变だ': '大變た', 'ロゲイン': '登录', '録': '录', '隊': '队', 'トトロ': 'ドドロ', 'ちん': 'ㄘん', 'イ': '亻', 'レ\(しなさい\)': '\(しなさい\)', 'ツ亻シター': 'ツイター', 'ⓃⒽⓀ': 'ⓀⓈ:m:', '紅': '红', '済': '济', '決': '决', 'ダ亻ソー': '名創優品', 'NHK': 'KSM', '极度': '極度', '静': '靜'}
for k in Correctlist:
    d1.append(k)
    d2.append(Correctlist[k])
print(d1)
print(d2)