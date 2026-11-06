// Only the bundled, redistributable examples are listed.
export const examples = Object.keys(import.meta.glob('../examples/*/index.tsx'))
  .map(path => path.split('/').at(-2)!)
  .sort()
  .map(id => ({ id, name: id.split('-').map(word => word[0].toUpperCase() + word.slice(1)).join(' '), kind: 'Scene', group: 'Scenes', note: 'StageShow example' }))
export const groups = ['Scenes']
