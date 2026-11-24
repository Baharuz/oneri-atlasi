export type Mode = 'close' | 'discover' | 'surprise';

export const modes: {value: Mode; label: string; description: string}[] = [
  {value: 'close', label: 'Benzer', description: 'Sevdiğin esere en yakın eşleşmeleri öne çıkar.'},
  {value: 'discover', label: 'Keşfet', description: 'Ortak yönleri koruyarak daha çeşitli eserler keşfet.'},
  {value: 'surprise', label: 'Şaşırt', description: 'Ortak yönleri olan eserler arasında çeşitliliğe daha fazla ağırlık ver.'},
];

export function RecommendationMode({value, onChange, disabled = false}: {
  value: Mode; onChange: (mode: Mode) => void; disabled?: boolean;
}) {
  return <fieldset className="recommendation-mode" disabled={disabled}>
    <legend>Nasıl öneriler istersin?</legend>
    {modes.map(mode => <label className="mode-option" key={mode.value}>
      <input type="radio" name="recommendation-mode" value={mode.value}
        checked={value === mode.value} onChange={() => onChange(mode.value)}/>
      <span><strong>{mode.label}</strong><small>{mode.description}</small></span>
    </label>)}
    <p>Her modda seçtiğin eser, tema ve atmosferler dikkate alınır. Sonuçlar kataloğa göre benzer olabilir.</p>
  </fieldset>;
}
