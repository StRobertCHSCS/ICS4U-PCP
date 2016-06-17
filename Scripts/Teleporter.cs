using UnityEngine;
using System.Collections;

public class Teleporter : MonoBehaviour {
	public Transform target;
	public float x;
	public float y;
	public float z;

	void OnCollisionEnter (Collision col) {
		if (col.gameObject.tag == "Player") {
			col.gameObject.transform.position = target.position + new Vector3(x, y, z);
		}
	}
}
